

function saveData()
{
	
	console.log("In saveData");
	var inp_name = document.getElementById("name1").value;
	var inp_birth_date = document.getElementById("date1").value;
	console.log(inp_name,inp_birth_date);
	eel.saveData(inp_name,inp_birth_date);
	eel.flagValue()(function(flag){
		//alert("I am here");
		//alert(flag);
		if(flag==1)
		{
			        alert("Record Added Successfully");
		}
		else
		{
			        alert("Error in adding record");
		}

	});
	
}

 
function printData()
{
	console.log("In printData")
	console.log("In printData")
	console.log("In printData")
	console.log("In printData")
	console.log("In printData")

}
function goBack() {
	console.log("In goBack")
  	window.history.back();
}


function getPathToFile() {
     eel.pythonFunction()(function(path){
     console.log(path.length);

     if(path.length != 0)
     {
     	document.getElementById("label1").innerHTML = "Uploaded";
     }

	});

}
function sendGreetings()
{
	window.open('https://web.whatsapp.com/', '_blank');
}


function fetchData()
{
	console.log("In Javascript")
	var size = [1216,739];



	eel.readBlobData()(function(name){
		//var name1 = name.split(",");
		
		console.log(name);
		if(name.length != 0)
		{
			var name1 = String(name).split(",");
			var initial = (name1.length/2);
			var j,k=0;
			var path=[];
			var person_name=[];

			for(j=0;j<initial;j++)                             //
			{                                                  //Spliting of Data
				person_name[k]=name1[j];                       //  into                          
				k++;                                           // person_name and path
			}
			j=0;                                               // from
			k=0;                                               // Python

			for(j=initial;j<name1.length;j++)                   //program
			{                                                   // main.py
				path[k]=name1[j];                               //
				k++;                                             //
			}                                                   //
			 
			console.log(person_name);
			console.log(path);

			console.log("here length is",person_name.length);
			var x ="", i;
			
			for (i=0; i<person_name.length; i++) 
			{
			
		 	x = x + "<div " + "id=" + "column " + ">" + "<img src=" + "/pics/" + path[i] + ".jpg" + " alt=" + "Avatar " + "style=" + "width:100% " + ">"  + "<div " + "id=" + "container " + ">" + "<h4>" + "<b>" + person_name[i] + "</b>" + "</h4>" + "<input " + "type=" + "button " + "id=" + "sub " + "value=" +"Send" + "Greetings " +"onclick=" +"sendGreetings() "+ ">"+ "</div>" + "</div>"; 
			}
		}
		else
		{
			x = "<h1 " + "id=" + "nobirth" + ">" + "There is no birthday today" + "</h1>";
		}
		console.log("x is",x);
		document.getElementById("row").innerHTML = x;
	})
	
	
}




