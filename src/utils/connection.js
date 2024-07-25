const { Sequelize } = require('sequelize');
require('dotenv').config();
const path = require('path');

// Configuración para SQLite
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: path.join(__dirname, '..', 'database', 'database.sqlite'), // Ruta al archivo de la base de datos
  logging: false
});

module.exports = sequelize;
