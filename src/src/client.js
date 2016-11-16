var React = require("react");
var ReactDOM = require("react-dom");
var xhr = require("xhr");

// Create your front-end app here
var main = React.createClass({
  getInitialState: function(){
    return {pagina: 'home', info: {}, value: 0, value2: 0, users: {}};//, "func": 0, "equip": 0};
    //count: 0};
  },
  setHome: function(){
    this.setState({pagina: 'home'});
  },
  setRequisicao: function(){
    this.setState({pagina: 'requisicao', value: 0, value2: 0});
    this.getEquipamentos();
    this.getUsers();
  },
  setGestao: function(){
    this.setState({pagina: 'gestao', value: 0});
    this.getEquipamentos();
  },
  setEquipamentos: function(){
    this.setState({pagina: 'equipamentos'});
    this.getEquipamentos();
  },

  getEquipamentos: function(){
    xhr.get("/equips", (err, res) => {
      this.setState({info: JSON.parse(res.body)});
    });
  },
  getUsers: function(){
    xhr.get("/users", (err,res) => {
      this.setState({users: JSON.parse(res.body)});
    })
  },
  requisitarManutencaoPost: function(){
    console.log(this.state.value);
    xhr.post("/requisitar/"+String(this.state.value), function(err, res){
        alert(res.body);
    });
  },
    realizarManutencaoPost: function(){
        console.log(this.state.value);
        xhr.post("/realizarmanutencao/"+String(this.state.value), function(err, res){
            alert(res.body);
        });
    },
    liberarEquipamentoPost: function(){
        console.log(this.state.value);
        xhr.post("/liberar/"+String(this.state.value), function(err, res){
            alert(res.body);
        });
    },
  componentDidMount: function(){
    state = this.state;
    set = this.setState.bind(this);
  },
  handleChange: function(event){
    this.getEquipamentos();
    this.setState({value: event.target.value})
  },
  handleChange2: function(event){
    this.setState({value2: event.target.value})
  },
  /*
  handleChange: function(field){
    return function(event) {
        this.setState({field: event.target.value});
      };
  },*/

  paginaHome: function(){
  	return <div>
  	<div><button onClick={this.setHome}> Home </button> 
  	<button onClick={this.setRequisicao}> Requisitar Manutenção </button>
  	<button onClick={this.setGestao}> Gerir Manutenção </button>
  	<button onClick={this.setEquipamentos}> Listar Equipamentos </button></div>
    <div>Bem vindo ao sistema Equador</div>
  	</div>;
  },
  paginaRequisicao: function(){
      var organize = function(obj){
          var lines = [];
          for(var key in obj){
              lines.push(<option key={key} value={key}>{obj[key].nome}</option>);
          };
          return <div><select value={this.state.value} onChange = {this.handleChange}>
              <option defaultValue disabled>Choose here</option>
              {lines}
          </select></div>;
      }.bind(this);
      var orgUsers = function(obj){
          var lines = [];
          count = 1;
          for(var key in obj){
            if (obj[key] === "Funcionario"){
              lines.push(<option key={count} value={count}>{key}</option>);
              count += 1;
            }
          };
          return <div><select value={this.state.value2} onChange = {this.handleChange2}>
              <option defaultValue disabled>Choose here</option>
              {lines}
          </select></div>;
      }.bind(this);

      return <div>
          <div><button onClick={this.setHome}> Home </button>
              <button onClick={this.setRequisicao}> Requisitar Manutenção </button>
              <button onClick={this.setGestao}> Gerir Manutenção </button>
              <button onClick={this.setEquipamentos}> Listar Equipamentos </button></div>
          <div> Requisitar Manutenção </div>
          <div> Equipamentos </div>
              <div> {organize(this.state.info)}</div>
          <div> Funcionários </div>
              <div> {orgUsers(this.state.users)}</div>
              <div><button onClick={this.requisitarManutencaoPost}> Requisitar </button></div>
          </div>;
  },
  paginaGestao: function(){
      var organize = function(obj){

          if (!this.state.value){
              for(var key in obj){
                  this.state.value = key;
                  break;
              }
          }


          var lines = [];
          for(var key in obj){
              lines.push(<option key={key} value={key}>{obj[key].nome}</option>);
          };
          return <div><select value={this.state.value} onChange={this.handleChange}>
              <option defaultValue disabled>Choose here</option>
              {lines}
              </select></div>;
      }.bind(this);
      this.getEquipamentos();
      return <div>
          <div><button onClick={this.setHome}> Home </button>
              <button onClick={this.setRequisicao}> Requisitar Manutenção </button>
              <button onClick={this.setGestao}> Gerir Manutenção </button>
              <button onClick={this.setEquipamentos}> Listar Equipamentos </button></div>
          <div> Gestão de Manutenção </div>
          <div> Equipamentos </div>
          <div> {organize(this.state.info)}</div>
          <div><button disabled={this.state.info[String(this.state.value)].status != 2} onClick={this.realizarManutencaoPost}> Realizar Manutenção </button></div>
          <div><button disabled={this.state.info[String(this.state.value)].status != 1} onClick={this.liberarEquipamentoPost}> Liberar Equipamento </button></div>
      </div>;
  },
  paginaEquipamentos: function(){
    var organize = function(obj){
      var lines = [];
      for(var key in obj){
        lines.push(<li key={key}><div className="item">Nome:</div>{obj[key].nome}
        <p><div className="item">Fabricante:</div>{obj[key].fabricante}</p>
        <p><div className="item">Local:</div>{obj[key].local}</p>
        <p><div className="item">Status:</div>{obj[key].status_t}</p></li>);
      };
      return <div><ol>{lines}</ol></div>;
    };
  	return <div>
    <div><button onClick={this.setHome}> Home </button> 
    <button onClick={this.setRequisicao}> Requisitar Manutenção </button>
    <button onClick={this.setGestao}> Gerir Manutenção </button>
    <button onClick={this.setEquipamentos}> Listar Equipamentos </button></div>
    <div>Pesquisa: </div>
    <div className="subtitle"> Equipamentos </div>
    <div> {organize(this.state.info)} </div>
    </div>;
  },


  /*
  dec: function(){
    this.setState({count: this.state.count - 1});
  },
  inc: function(){
    this.setState({count: this.state.count + 1});
  },
  save: function(){
    xhr.post("/save/"+String(this.state.count), function(err, res){
      alert(res.body);
    });
  },
  load: function(){
    xhr.get("/load", (err, res) => {
      this.setState({count: Number(res.body)});
    });
  },*/
  render: function(){
  	if (this.state.pagina === 'home') {
  		return this.paginaHome();
  	}
  	if (this.state.pagina === 'requisicao') {
  		return this.paginaRequisicao();
  	}
  	if (this.state.pagina === "gestao") {
  		return this.paginaGestao();
  	}
  	if (this.state.pagina === "equipamentos") {
  		return this.paginaEquipamentos();
  	}
    /*return <div>
      <div>Count: {this.state.count}</div>
      <div>
        <button onClick={this.dec}>- 1</button>
        <button onClick={this.inc}>+ 1</button>
        <button onClick={this.save}>Save</button>
        <button onClick={this.load}>Load</button>
      </div>
    </div>;
    */
  }
});

window.onload = function(){
  ReactDOM.render(
    React.createElement(main),
    document.getElementById("main"));
};
