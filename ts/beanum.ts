namespace mariucol {
	declare const steam: unique symbol;
	declare const amazon: unique symbol;
	declare const games: unique symbol;
	declare const sex: unique symbol;
	declare const gas: unique symbol;
	declare const parking: unique symbol;
	declare const transport_id: unique symbol;
	
	declare type steam = typeof steam;
	declare type amazon = typeof amazon;
	declare type games = typeof games;
	declare type sex = typeof sex;
	declare type gas = typeof gas;
	declare type parking = typeof parking;
	declare type transport_id = typeof transport_id;
	
	type id = unknown;
	
	type payee = steam | amazon | id;
	type transport = gas | parking | transport_id;
	type category = sex | games | transport | id;
	export type account = payee & category;
}
