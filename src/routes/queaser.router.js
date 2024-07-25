const { getAll, create, remove, update } = require('../controllers/queaser.controllers');
const express = require('express');
const verifyJWT = require('../utils/verifyJWT');

const routerQueaser = express.Router();

routerQueaser.route('/')
	.get(verifyJWT, getAll)
	.post(verifyJWT,create)
routerQueaser.route("/:id")
    .delete(verifyJWT,remove)
	.put(verifyJWT,update)

module.exports = routerQueaser;