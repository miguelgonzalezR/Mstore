<?php
include '{{ STATIC_URL }}/php/jconfig.php';
class MySQL
{
    private $oConBD = null;

    public function __construct()
    {
        global $usuarioBD, $passBD, $ipBD, $nombreBD;
        $this->usuarioBD = $usuarioBD;
        $this->passBD = $passBD;
        $this->ipBD = $ipBD;
        $this->nombreBD = $nombreBD;
    }

    /**
     * Conexión BD por PDO
     */
    public function conBDPDO()
    {
        try {
            $this->oConBD = new PDO("mysql:host=" . $this->ipBD . ";dbname=" . $this->nombreBD, $this->usuarioBD, $this->passBD);
            return true;
        } catch (PDOException $e) {
            echo "Error al conectar a la base de datos: " . $e->getMessage() . "\n";
            return false;
        }
    }


    public function getDatosGrafica()
    {
        $jDatos = '';
        $rawdata = array();
        $i = 0;
        try {

            $strQuery = "SELECT shop_product.name , sum(orders_orderitem.quantity) as ventas 
            from shop_product, orders_orderitem
            WHERE shop_product.id = orders_orderitem.product_id
            group by shop_product.name";

            # $strQuery = "SELECT nombre ,sum(precio) as tPrecio, SUM(cantidad_vendidos) as tVendidos
            #,DATE_FORMAT(fecha_alta, '%Y-%m-%d') as fecha FROM resumen_productos GROUP BY DATE_FORMAT(fecha_alta, '%Y-%m-%d')";
            
            if ($this->conBDPDO()) {
                $pQuery = $this->oConBD->prepare($strQuery);
                $pQuery->execute();
                $pQuery->setFetchMode(PDO::FETCH_ASSOC);
                while($producto = $pQuery->fetch()) {
                    $oGrafica = new Grafica();
                    $oGrafica->Nombre = $producto['name'];
                    $oGrafica->totalPrecio = $producto['ventas'];
                    $rawdata[$i] = $oGrafica;
                    $i++;
                }
                $jDatos = json_encode( $rawdata);
            }
        } catch (PDOException $e) {
            echo "MySQL.getDatosGrafica: " . $e->getMessage() . "\n";
            return -1;
        }
        return $jDatos;
    }

}
class Grafica{
    public $totalPrecio = 0; 
}
