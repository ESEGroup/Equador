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
    "nome": "Ar Condicionado",
    "status": 0,
    "status_t": "Disponível",
    "fabricante": "A",
    "local": "H-310"
  },
  "2": {
    "nome": "Lâmpada",
    "status": 1,
    "status_t": "Em Manutenção",
    "fabricante": "B",
    "local": "H-204"
  },
  "3": {
    "nome": "Cadeira",
    "status": 2,
    "status_t": "Manutenção Pendente",
    "fabricante": "C",
    "local": "A-624"
  }
}

var usuarios = {
	'Thiago': 'Funcionario',
	'Guilherme': 'Administrador',
    "fabricante": "A",
    "local": "H-310"
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

app.post("/realizarmanutencao/:value", function(req, res){
    value = req.params.value;
    if (equipamentos[value] && equipamentos[value].status == 2){
        equipamentos[value].status = 1;
        res.send("Manutenção está agora em andamento");
    }
    else{
        res.send("Erro ao colocar manutenção em andamento");
    }

});

app.post("/liberar/:value", function(req, res){
    value = req.params.value;
    if (equipamentos[value] && equipamentos[value].status == 1){
        equipamentos[value].status = 0;
        res.send("Equipamento liberado de manutenção");
    }
    else{
        res.send("Erro ao liberar equipamento");
    }

});

app.get("/load", function(req, res){
  res.send(String(value));
});
