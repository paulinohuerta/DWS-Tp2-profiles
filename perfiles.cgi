#!/usr/bin/perl 

use CGI;
use utf8;

#Declaramos la entrada del CGI.
$perlcgi = new CGI;

#El formulario que vamos a usar.
if(!$perlcgi->param){
    print $perlcgi->header(-charset => 'iso8859-1');
    print $perlcgi->start_html('Perfiles');
    print $perlcgi->start_form(-onsubmit=>'/submit');
    	#Ahora le damos forma a la vista.
    print $perlcgi->h1('Introduzca los datos del nuevo perfil');
    print $perlcgi->br;
  	  #Ahora introduciremos los campos variados  
    print $perlcgi->h2('Nombre y apellidos ');
    print $perlcgi->h3('Nombre:');
    print $perlcgi->textfield(-name=>'nombre',-size=>10,-maxlength=>60);
    print $perlcgi->h3('Apellidos:');
    print $perlcgi->textfield(-name=>'apellidos',-size=>25,-maxlength=>80);
    print $perlcgi->h2('Grupo: ');
    print $perlcgi->h3('¿A que grupo pertenece?');
    print $perlcgi->radio_group(-name=>'grupo',-values=>['Amigos', 'Familia', 'Trabajo', 'Conocidos/otros'],-defaults =>'Amigos',-columns=>2,-rows=>2);
    print $perlcgi->h2('Tlf móvil:');
    print $perlcgi->textfield(-name=>'tlfmovil',-size=>10,-maxlength=>60); 
    print $perlcgi->h2('Tlf fijo:');
    print $perlcgi->textfield(-name=>'tlffijo',-size=>10,-maxlength=>60); 
   	 #Y acabamos el form no sin antes poner los botones. 
    print $perlcgi->submit('submit','Enviar');
    print $perlcgi->reset('reset','Limpiar');
    print $perlcgi->end_form;
    
} else {
    #Usamos las variables para meterlas en un documento nuevo (sin sobreescribir, para almacenar varios perfiles si queremos). 
    print $perlcgi->header(-charset => 'iso-8859-1');
    print $perlcgi->start_html('Perfiles almacenados: ');
    my $nombre = $perlcgi->param('nombre');
    my $apellidos = $perlcgi->param('apellidos');
    my $grupo = $perlcgi->param('grupo');
    my $tlfmovil = $perlcgi->param('tlfmovil');
    my $tlffijo = $perlcgi->param('tlffijo');

     open F, '>>/tmp/perfiles.txt' or die "Imposible abrir el fichero:$!";
	#Ahora mostraremos los datos de los perfiles almacenados en el fichero de texto.
     print F "Nombre: $nombre \n Apellidos: $apellidos \n Grupo: $grupo \n Nº Movil: $tlfmovil \n Nº Fijo: $tlffijo \n";
     close F;
	#Abrimos el documento creado
	open F, '/tmp/perfiles.txt' or die "Imposible abrir el fichero:$!";
	#Lo recorremos y lo vamos imprimiendo
    while(<F>) {
    print "$_ <br>";
    }
	#Finalmente cerramos
    close F;
}
