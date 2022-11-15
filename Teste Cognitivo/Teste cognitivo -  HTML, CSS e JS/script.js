var cronometro=60;
var indiceImg=0;
var indicePonto=0;
var indiceAcertos=0;
var indiceErros=0;
var controle=false;
var controlaJogo=true;
var primeiroClick=true;
var valorPlacar=0;
var fig;
var cor;
var div;
var valorFig;
var valorCor;
var valorDiv;
var tempo;

var aperteiFig=false;
var aperteiCor=false;
var aperteiDiv=false;

function relogio(){
	cronometro-=1;
	if(cronometro<=0){
		clearInterval(tempo);
		controlaJogo=false;
		var telaMsg=document.getElementById("telaMsg");
		telaMsg.style.backgroundImage="URL('img/final.png')";
		telaMsg.style.display="block";
		var p=document.createElement("p");
		var attId=document.createAttribute("id");
		attId.value="textoFinal";
		p.setAttributeNode(attId);
		attStyleTexto=document.createAttribute("style");
		attStyleTexto.value="color: #00f;top: 0%;font-weight: 1000;font-family: 'Anton', sans-serif;";
		p.setAttributeNode(attStyleTexto);
		telaMsg.appendChild(p);
		var resultado;
		if(valorPlacar<=9){	
			resultado="Atenção ruim."
		}
		else if((valorPlacar>=10)&&(valorPlacar<=19)){
			resultado="Atenção normal."
		}
		else{
			resultado="Atenção boa"
		}
		document.getElementById("textoFinal").innerHTML="Acertos: "+indiceAcertos+"<br>Erros: "+indiceErros+"<br>Pontos: "+valorPlacar+"<br>Resultado:"+resultado;
		window.removeEventListener("keydown",keydown);
	}
	document.getElementById("rel").value=cronometro+"s";
}
function erro(){
	if(controle==true){
		console.log("idDiv: "+("img"+indiceImg)+"\n");
		const music=new Audio('som/errado.mp3');
		music.play();
		indiceErros++;
	}
	jogo();
	if(primeiroClick==false){
		valorPlacar--;
	}
	if(valorPlacar<=0){
		valorPlacar=0;
	}
	document.getElementById("placar").value=valorPlacar;
}
function acerto(){
	if(controle==true){
		const music=new Audio('som/acerto.mp3');
		music.play();
		indiceAcertos++;
	}
	jogo();
	if(primeiroClick==false){
		valorPlacar++;
	}
	document.getElementById("placar").value=valorPlacar;
}
function keydown(){
	console.log("===========================================");
	var tecla=event.keyCode;
	console.log("Tecla: "+tecla+"\n");
	if(
		(tecla!=37)&&(tecla!=38)&&(tecla!=39)&&(tecla!=40)&&(tecla!=32)&&(tecla!=96)&&(tecla!=87)&&(tecla!=83)&&(tecla!=68)&&(tecla!=65)||
		((tecla==37)&&(fig!=0))||((tecla==38)&&(fig!=1))||((tecla==39)&&(fig!=2))||((tecla==40)&&(fig!=3))||
		((tecla==87)&&(cor!=0))||((tecla==83)&&(cor!=1))||((tecla==68)&&(cor!=2))||((tecla==65)&&(cor!=3))||
		((tecla==32)&&(div!=0))||((tecla==96)&&(div!=1))
	){
		console.log("Erro 1: Tecla Errada\n");
		indicePonto=0;
		erro();
	}else{
		if((((tecla==32)&&(div==0))||((tecla==96)&&(div==1)))&&((aperteiCor==true)&&(aperteiFig==true)&&(aperteiDiv==false))){
			aperteiDiv=true;
			console.log("Erro 2\n");
			if(primeiroClick==false){
				indicePonto++;
			}
		}
		else if((((tecla==87)&&(cor==0))||((tecla==83)&&(cor==1))||((tecla==68)&&(cor==2))||((tecla==65)&&(cor==3)))&&
			((aperteiFig==true)&&(aperteiDiv==false)&&(aperteiCor==false))){
			aperteiCor=true;
			console.log("Erro 3\n");
			if(primeiroClick==false){
				indicePonto++;
			}
		}
		else if((((tecla==37)&&(fig==0))||((tecla==38)&&(fig==1))||((tecla==39)&&(fig==2))||((tecla==40)&&(fig==3)))&&
			((aperteiCor==false)&&(aperteiDiv==false)&&(aperteiFig==false))){
			aperteiFig=true;
			console.log("Erro 4: Clicou nas teclas \"fig\"\n");
			if(primeiroClick==false){
				indicePonto++;
			}
		}
		else{
			console.log("Erro 1: Tecla Errada\n");
			indicePonto=0;
		erro();
		}
		if(indicePonto>=3){
			indicePonto=0;
			acerto();
		}
	}
	primeiroClick=false;
	console.log("aperteiFig:"+aperteiFig+"\n");
	console.log("aperteiCor:"+aperteiCor+"\n");
	console.log("aperteiDiv:"+aperteiDiv+"\n");
	console.log("indicePonto: "+indicePonto+"\n");
}
function jogo(){
	if(controlaJogo==true){
		if(controle==true){
			document.getElementById("img"+(indiceImg-1)).remove();
		}
		fig=Math.floor(Math.random()*4);
		console.log("Figura: "+fig+"\n");
		cor=Math.floor(Math.random()*4);
		console.log("Cor: "+cor+"\n");
		div=Math.floor(Math.random()*2);
		console.log("Div: "+div+"\n");
		var obj=document.getElementById("principal"+div);
		var novaImg=document.createElement("img");//Cria nova div
		var att1=document.createAttribute("id");
		var att2=document.createAttribute("src");
		var att3=document.createAttribute("style");
		att1.value="img"+indiceImg;
		switch(fig){
			case 0:
				att2.value="img/circulo/"+cor+".png";
				break;
			case 1:
				att2.value="img/pentagono/"+cor+".png";
				break;
			case 2:
				att2.value="img/quadrado/"+cor+".png";
				break;
			case 3:
				att2.value="img/triangulo/"+cor+".png";
				break;
			default:
				console.log("Erro desconhecido ao imprimir imagem na tela\n");
				break;
		}
		att3.value="border: 5px solid #000";
		novaImg.setAttributeNode(att2);//Adiciona atributo "att2" na "img"
		novaImg.setAttributeNode(att3);
		novaImg.setAttributeNode(att1);
		obj.appendChild(novaImg);
		indiceImg++;
		if(controle!=true){
			tempo=setInterval(relogio,1000);
			document.getElementById("telaMsg").style.display="none";
		}
		controle=true;
		aperteiFig=false;
		aperteiCor=false;
		aperteiDiv=false;
	}
}
window.addEventListener("keydown",keydown);
//************************************************
/*
	Amarelo: 0
	Azul: 1
	Verde: 2
	Vermelho: 3

	w=Amarelo
	s=Azul
	a=Vermelho
	d=Verde

	Esquerda=círculo
	Cima=pentágono
	Direita=quadrado
	Baixo=triangulo
*/