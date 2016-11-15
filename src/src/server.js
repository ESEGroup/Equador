var express = require("express");
var app = express();
app.use(express.static("app"));
app.listen(3000, function(){
  console.log("Serving app on http://localhost:3000/");
});


// Create your back-end logic here

var value = 0;

var equipamentos = {
  "1": {
    "nome": "ar condicionado",
    "status": 0,
    "status_t": "Disponível"
  },
  "2": {
    "nome": "lâmpada",
    "status": 1,
    "status_t": "Em Manutenção"
  },
  "3": {
    "nome": "cadeira",
    "status": 2,
    "status_t": "Manutenção Pendente"
  }
}

var usuarios = {
	'Thiago': 'Funcionario',
	'Guilherme': 'Administrador'
}

app.get("/equips", function(req,res){
	res.send(JSON.stringify(equipamentos));
});

app.post("/requisitar/:value", function(req, res){
  value = req.params.value;
  if (equipamentos[value] && equipamentos[value].status == 0){
      equipamentos[value].status = 2;
      res.send("Manutenção requisitada com sucesso");
  }
  else{
      res.send("Erro ao requisitar manutenção");
  }

});

app.get("/load", function(req, res){
  res.send(String(value));
});
