# Aaron Perez Esparza 1993809
$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "==Determinando tu gateway ..."
Write-Host "Tu gateway es: $subred"
$rango = $subred.Substring(0, $subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') + 1).IndexOf('.') + 3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango
$punto = $rango.EndsWith('.')
if($punto -like "False" )
{
   $rango = $rango + '.'
}
$rango_ip = @(19..1)
Write-output ""
Write-Host "-- Subred actual:"
Write-Host "Escanenado: "-NoNewline ; Write-Host "0/24" -Foregroundcolor Red
Write-output ""
foreach( $r in $rango_ip ){ $actual = $rango + $r 
    $respuesta = Test-connection $actual -Quiet -Count 1 
    if ( $respuesta -eq "True"){
        Write-output " "
        Write-Host " Host responde: " -NoNewline; Write-Host $respuesta -ForegroundColor Green
    }
}
