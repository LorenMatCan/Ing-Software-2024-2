import { Container } from "react-bootstrap"
import { Row } from "react-bootstrap"
import { Col } from "react-bootstrap"
import { Button } from "react-bootstrap"
import { useState } from "react"


export function ActualizarRentas({rentas,funcion}) {
    const [RentaSelecionada, setRentaSe] = useState(undefined);
    const [renta, setRenta] = useState(false);
    const [id, setId] = useState(0);

    const handleId = (event) => {
        setId(event.target.value);
    }
    
    const buscarRenta = () => {
        const idN = parseInt(id);
        const rentaEditar = rentas.find((ren) => ren.id === idN);
    
        if (rentaEditar!==undefined){
            setRentaSe(rentaEditar);
            setRenta(true)
        }
        else{
            setRenta(false)
        }
    }




    return (
        <div>   
        <h3>Actualizar Renta</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number" onChange={handleId}/>
                <Button variant="outline-light" onClick={buscarRenta}>Buscar</Button>
                </Col>
            </Row>
            {renta ? <ActualizarRenta id = {id} funcion={funcion} rentas={rentas} rentaAE={RentaSelecionada} estado={setRenta}/> : "Renta no encontrada"}
            
        </Container>
        </div>
    )

    
}

function ActualizarRenta(prop){

    function entregado(){
        prop.rentaAE.estado = "1";
        prop.funcion(prop.rentas);
        prop.estado(false);
    }

    function noEntregado(){
        prop.rentaAE.estado = "0";
        prop.funcion(prop.rentas);
        prop.estado(false);
    }

    return (
        <div>
            <h3>Información de la renta</h3>
            <Container>
                <table>
                    <tr>
                        <td>id:</td>
                        <td>{prop.rentaAE.id}</td>
                    </tr>
                    <tr>
                        <td>idUsuario:</td>
                        <td>{prop.rentaAE.idUsuario}</td>
                    </tr>
                    <tr>
                        <td>idPelicula:</td>
                        <td>{prop.rentaAE.idPelicula}</td>
                    </tr>
                    <tr>
                        <td>fechaRenta:</td>
                        <td>{prop.rentaAE.fechaRenta}</td>
                    </tr>
                    <tr>
                        <td>dias de renta:</td>
                        <td>{prop.rentaAE.dias}</td>
                    </tr>
                    <tr>
                        <td>estado:</td>
                        <td>{prop.rentaAE.estado}</td>
                    </tr>
                    <tr>
                        <td><Button variant="outline-light" onClick={entregado}>Entregada</Button></td>
                        <td><Button variant="outline-light" onClick={noEntregado}>No ha sido devuelta</Button></td>
                    </tr>
                </table>

            </Container>
        
            
       
        </div>
    )
}