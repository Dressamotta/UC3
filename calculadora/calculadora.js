document.addEventListener("DOMContentLoaded", function () {
    const display = document.getElementById("display");
  
    function adicionar(valor) {
      display.value += valor;
    }
  
    function limpar() {
      display.value = "";
    }
  
    function calcular() {
      try {
        display.value = new Function("return " + display.value)();
      } catch {
        display.value = "Erro";
      }
    }
  
    // Torna as funções acessíveis aos botões
    window.adicionar = adicionar;
    window.limpar = limpar;
    window.calcular = calcular;
  });
  