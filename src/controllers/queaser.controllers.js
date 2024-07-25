const catchError = require('../utils/catchError');
const Queaser = require('../models/Queaser');

const getAll = catchError(async(req, res) => {
	const queaser = await Queaser.findAll({include: [Dia]})
	return res.json(queaser)
});


const create = catchError(async (req, res) => {
	// Asumiendo que la información del usuario está disponible en req.user
	const userId = req.user.id;
  
	const queaser = await Queaser.create({
	  ...req.body,
	  userId: userId, // Asignar el ID del usuario a la propiedad userId
	});
  
	return res.status(201).json(queaser);
  });

const remove = catchError(async(req, res) => {
	const removeQueaser = await Queaser.destroy({where: [req.params]})
	return res.sendStatus(204)
})
const update = catchError(async(req, res) => {
	const body = req.body
	const {id} = req.params
	const updateQueaser = await Queaser.update(body, {where: {id}, returning: true})
	if(updateQueaser[0] === 0) return res.status(404).json({message: "no existe"})
	return res.json(updateQueaser)
})

module.exports = {
	getAll,
	create,
	remove, 
	update
}