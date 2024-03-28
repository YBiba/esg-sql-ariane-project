DROP TABLE IF EXISTS production_energies_renouvelables;
DROP TABLE IF EXISTS consommation_energetique;
DROP TABLE IF EXISTS batiments;

create table production_energies_renouvelables( 
	id_production char(4) PRIMARY KEY,
	id_batiment char(4),
	quantite_produite integer,
	type_energie_renouvelable varchar,
	date_production date);
	
create table consommation_energetique( 
	id_consommation char(4) PRIMARY KEY,
	id_batiment char(4),
	consommation_kwh float,
	type_energie varchar,
	date_consommation date
);

create table batiments( 
	id_batiment char(4) PRIMARY KEY,
	nom_batiment varchar,
	surface float,
	annee_construction char(4)
);