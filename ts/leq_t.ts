export declare const dummy;

declare const adhoc: unique symbol;
type discriminator = {[_ in typeof adhoc]: void};
type safe_range = number[] & discriminator; // Requires length of at least 1

type is_range_rec<range_unsafe extends number[]> =
	range_unsafe extends [...infer head, infer tail]
		? head extends number[]
			? tail extends head["length"]
				? head["length"] extends tail
					? is_range_rec<head>
					: false
				: false
			: false
		: true

export type is_range<range_unsafe> =
	range_unsafe extends number[]
		? range_unsafe extends []
			? false
			: is_range_rec<range_unsafe>
		: false

type digit<digits extends safe_range> = digits[number]
type num<digits extends safe_range> = digit<digits>[]
type digit_pred<digits extends safe_range, i extends number> =
	digits extends infer digits_u & discriminator
		? digits_u extends number[]
			? [false,...digits_u][i] extends digit<digits>
				? [false,...digits_u][i]
				: never
			: never
		: never
type fst_digit<digits extends safe_range> = digits[0]
type lst_digit<digits extends safe_range> =
	digit_pred<digits, digits["length"]> extends number
		? digits[digit_pred<digits, digits["length"]>]
		: never

type pred_carry_u<digits extends safe_range, pred_head extends number[] | false> =
	pred_head extends number[]
		? pred_head extends [fst_digit<digits>]
			? [lst_digit<digits>]
			: [...pred_head, lst_digit<digits>]
		: false

type pred_u<digits extends safe_range, n extends num<digits>> =
	n extends [...infer head, infer tail]
		? tail extends fst_digit<digits>
			? head extends num<digits>
				? pred_carry_u<digits, pred_u<digits, head>>
				: false
			: tail extends digit<digits>
				? [...head, digit_pred<digits, tail>]
				: false
		: false

type leq_u1<digits extends safe_range, n extends unknown> = n extends num<digits> ? leq_u<digits, n> : never
type leq_u<digits extends safe_range, n extends num<digits>> =
	n extends [fst_digit<digits>]
		? [fst_digit<digits>]
		: n | leq_u1<digits, pred_u<digits, n>>

export type pred<digits, n> = 
	digits extends number[]
		? is_range<digits> extends never
			? never
			: n extends num<digits & discriminator>
				? pred_u<digits & discriminator, n>
				: never
		: never
export type leq<digits, n> = 
	digits extends number[]
		? is_range<digits> extends never
			? never
			: n extends num<digits & discriminator>
				? leq_u<digits & discriminator, n>
				: never
		: never

type D_u = [0,1,2,3,4,5]
type leq_14_b5 = leq<D_u, [1,4]>

// type pred_24 = pred_u<D, N>;

// const x: leq_24 = [1, 6]; // ok
// const y: leq_24 = [2, 6]; // not ok

