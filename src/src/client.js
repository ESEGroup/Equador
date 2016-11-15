var React = require("react");
var ReactDOM = require("react-dom");
var xhr = require("xhr");

// Create your front-end app here
var main = React.createClass({
  getInitialState: function(){
    return {pagina: 'home', info: {}};
    //count: 0};
  },
  setHome: function(){
    this.setState({pagina: 'home'});
  },
  setRequisicao: function(){
    this.setState({pagina: 'requisicao'});
  },
  setGestao: function(){
    this.setState({pagina: 'gestao'});
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
  componentDidMount: function(){
    state = this.state;
    set = this.setState.bind(this);
  },

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
  	return <div>
    <div><button onClick={this.setHome}> Home </button> 
    <button onClick={this.setRequisicao}> Requisitar Manutenção </button>
    <button onClick={this.setGestao}> Gerir Manutenção </button>
    <button onClick={this.setEquipamentos}> Listar Equipamentos </button></div>
    <div> Requisição de Manutenção </div>
    </div>;
  },
  paginaGestao: function(){
  	return <div>
    <div><button onClick={this.setHome}> Home </button> 
    <button onClick={this.setRequisicao}> Requisitar Manutenção </button>
    <button onClick={this.setGestao}> Gerir Manutenção </button>
    <button onClick={this.setEquipamentos}> Listar Equipamentos </button></div>
    <div> Gestão de Manutenção </div>
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
