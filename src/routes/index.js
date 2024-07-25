const express = require('express');
const routerQueaser = require('./queaser.router');
const routerUser = require('./user.router');
const router = express.Router();

// colocar las rutas aquí
router.use("/queaser", routerQueaser)
router.use("/user", routerUser)


module.exports = router;