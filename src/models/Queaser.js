const { DataTypes } = require('sequelize');
const sequelize = require('../utils/connection');
const User = require('./User');

const Queaser = sequelize.define('queaser', {
	name: {
		type: DataTypes.STRING,
		allowNull: false
	},
	horario: {
		type: DataTypes.STRING,
		allowNull: false
	},
	finalizado: {
		type: DataTypes.BOOLEAN,
		allowNull: false
	}
	});
	

module.exports = Queaser;