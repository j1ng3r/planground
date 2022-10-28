export declare const dummy;

const digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] as const;
const pred = [,...digits] as const;
const last = digits[digits.length - 1];
type last = typeof last;

type digit = typeof digits[number];
type num = digit[] | never;

type pred_carry<pred_head extends num> =
	pred_head extends never
		? never
		: pred_head extends [0]
			? [last]
			: [...pred_head, last]

type pred<n extends num> =
	n extends [...infer head, infer tail]
		? tail extends 0
			? head extends num
				? pred_carry<pred<head>>
				: never
			: tail extends digit
				? [...head, typeof pred[tail]]
				: never
		: never

type leq<n extends num> = n extends [0] ? [0] : n | leq<pred<n>>;

type leq_24 = leq<[2, 4]>

const x: leq_24 = [1, 6]; // ok
// const y: leq_24 = [2, 6]; // not ok

