const Queaser = require("./Queaser");
const User = require("./User");

User.hasMany(Queaser)
Queaser.belongsTo(User)
