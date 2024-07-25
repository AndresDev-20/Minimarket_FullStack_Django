const { DataTypes } = require('sequelize');
const sequelize = require('../utils/connection');
const bcrypt = require("bcrypt")

const User = sequelize.define('user', {
	name: {
		type: DataTypes.STRING,
		allowNull: false
	},
	surnames: {
		type:DataTypes.STRING,
		allowNull: false
	},
	email: {
		type: DataTypes.STRING,
		allowNull: false,
		unique: true
	},
	password: {
		type: DataTypes.STRING,
		allowNull:false
	}

});

User.prototype.toJSON = function(){
    const values = Object.assign({}, this.get());
    delete values.password
    return values
};

User.beforeCreate(async(user)=>{
    const hashPassword = await bcrypt.hash(user.password, 10)
    user.password = hashPassword
})


module.exports = User;