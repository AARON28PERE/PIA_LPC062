# Aaron Perez Esparza 1993809
#Escaneo de equipos activos en la subred
#
# Determinado geteway
$subred =(Get-NetRoute -DestinationPrefix 0.0.0.0/0).NexHop
Write-Host"== Determinando tu gateway ..."
Write-Host "Tu gateway: $subred"
#
#Determinado el rango de subred
#
$rango = $subred.Substring(0,$subred.IndexOf('-') + 1 + $subred.Substring($subred.IndexOf('-') + 1).IndexOf('-') + 3)
Write-Host "==Determinando tu rango de subred ..."
echo $rango
#
##Determinado si $rango termina en "."
##En ocaciones el rango de subred no termina en punto, neseitamos forzarlo
#
$punto = $rango.Endswith('.')
if ( $punto --like "False" )
{
  $rango = $rango + '.' #agregamos el punto en caso de que no estuviera.
}
#
##creamos un array con 254 numeros (1 a 1) y se almacena
## en una variable que se llamara $rango_ip
$rango_ip =@(1..1)
#
## Generamos bucle foreach para validar hosts activos en nuestra subred
#
Write-output""
Write-Host "--subred actual:"
Write-output ""
foreach($r in $rango_ip)
{
    $actual = $rango + $r #se genera direccion ip
    $responsw = Test-connection $actual -Quiet -Count 1 #validamos conexion contra ip en $actual
    if ( $responde -eq "True")
    {
       Write-output""
       Write-Host " Host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green
    }
}
#
##Fin del script
#
