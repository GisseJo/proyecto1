$( document ).ready(function() {    


    $('.date-picker').datepicker( {
        changeMonth: false,
        changeYear: false,
        showButtonPanel: false,
        dateFormat: 'mm-yy',
            onChangeMonthYear:function(y, m, i){                                
        var d = i.selectedDay;
        $(this).datepicker('setDate', new Date(y, m-1, d));
        $('#fecha').html(y+'/'+m);
       // window.location.replace("/#algo");
window.location.hash = y+'-'+m;
    }

    });


//proposito_collection1 = new tabla.PropositoCollection();
//proposito_collection1.fetch({data:{"mes_ano_":"2013-09"}});


 //pparticular_collection= new tabla.PParticularCollection();
//pparticular_collection.fetch();






////////nuevo proposito/////////////////////
 /*var proposito_nuevo = new tabla.Proposito({ "vinculacion":"/api/vinculacion/1/", "mes_ano": "2013-09-01", "proposito": "rezar denahklrio"});
   proposito_nuevo.save({                     // se genera GET /usuarios/1
    success:function(){     
        alert("Creacion de una nuevo proposito" + JSON.stringfy(proposito_nuevo.attributes)); // imprime {"id":1, "nombre": "Alfonso", "apellidos": "Marin Marin"}
    }
});*/
/*
   var proposito_nuevo1 = new tabla.Proposito({id:22});  
    proposito_nuevo1.fetch({                     
    success:function(){
            alert('Traigo UN proposito '+ JSON.stringify(proposito_nuevo1.attributes)); //imprime los atributos            
        }
    });

*/


///////////////Traigo todas las Vinculaciones/////////////////////////////    
/*vinculacion_collection = new tabla.VinculacionCollection();
listaVinculacionView = new tabla.ListaVinculacionView({ collection: vinculacion_collection});
vinculacion_collection.fetch( {success:function(){
    //alert('Traigo todas las vinculaciones Cant: '+ vinculacion_collection.length);
    //alert('su meta es '+ JSON.stringify(vinculacion_collection.meta) )
    //alert('sus modelos son es '+ JSON.stringify(vinculacion_collection.models) )
       
    $('#vinculaciones').html(listaVinculacionView.render().el);
    vinculacion_collection.each(
            function(vinculacion) {
                //console.log(vinculacion.get("vinculacion"));
                //console.log(vinculacion.toJSON())
                //VinculacionView = new tabla.VinculacionView({ model: vinculacion, el: $("#sidebar-nuevo")});
        });
    } 
});*/
/*
    vinculacion1 = new tabla.Vinculacion({ vinculacion: "Nueva Vinculacion"});
    vinculacion1.set({prioridad:"alta"});
    var nombre_vinculacion = vinculacion1.get("vinculacion");
    vinculacion1.set({vinculacion:"Nueva Vinculacion2"});
    alert(nombre_vinculacion);
*/
///////////////TRaigo la MArcacion de id :2////////////////////////////
  /*  var marcacion_nueva1 = new tabla.Marcacion({id:65});  
    marcacion_nueva1.fetch({                     
    success:function(){
        marcacion_nueva1.set({cumplimiento:5});
            alert('Traigo UNA marcacion '+ JSON.stringify(marcacion_nueva1.attributes)); //imprime los atributos 			
        marcacion_nueva1.save();
        }
    });
*/
///////Creacion de una vinculacion////////////////////////////////////////
/*    var vinculacion_nueva = new tabla.Vinculacion({vinculacion:"jajajaja"});
    vinculacion_nueva.save({                     // se genera GET /usuarios/1
    success:function(){    	
        //alert("Creacion de una nueva vinculacion" + JSON.stringfy(vinculacion_nueva.attributes)); // imprime {"id":1, "nombre": "Alfonso", "apellidos": "Marin Marin"}
    }
});*/

 /*   ///////////////TRaigo la vinculacion de id :1////////////////////////////
    var vinculacion_nueva1 = new tabla.Vinculacion({id:1});  
    vinculacion_nueva1.fetch({                     
    success:function(){
    	vinculacion_nueva1.set({vinulacion:"cambie el nombre"});
    	vinculacion_nueva1.save();
          //  alert('Traigo UNA vinculacion '+ JSON.stringify(vinculacion_nueva1.attributes)); //imprime los atributos
        }
    });*/

///////////Destroy funciona de lujo
//var vinculacion_nueva3 = new tabla.Vinculacion({id:3});
//vinculacion_nueva3.destroy();
console.log( "ready!" );
});
