import { Container } from "react-bootstrap"
import { Row } from "react-bootstrap"
import { Col } from "react-bootstrap"
import { Button } from "react-bootstrap"
import { useState } from "react"


export function ActualizarUsuarios({usuarios,funcion}) {
    const [UsuarioSelecionado, setUsuarioSe] = useState(undefined);
    const [usuario, setUsuario] = useState(false);
    const [usuarioEditar, setUsuarioEditar] = useState("");   
    const [id, setId] = useState(0);
    const handleId = (event) => {
        setId(event.target.value);
    }
    
    const buscarUsuario = () => {
        const idN = parseInt(id);
        const usuarioEditar = usuarios.find((usr) => usr.id === idN);
        setUsuario(usuarioEditar);
        if (usuarioEditar!==undefined){
            setUsuarioEditar("");
            setUsuario(true)
            setUsuarioSe(usuarioEditar);
        }
        else{
            setUsuario(false)
        }
    }




    return (
        <div>   
        <h3>Actualizar Usuario</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number" onChange={handleId}/>
                <Button variant="outline-light" onClick={buscarUsuario}>Buscar</Button>
                </Col>
            </Row>
            {usuario ? <ActualizarUsuario id = {id} funcion={funcion} usuarios={usuarios} usuarioAE={UsuarioSelecionado} estado={setUsuario}/> : "Usuario no encontrado"}
            
        </Container>
        </div>
    )

    
}


function ActualizarUsuario ({id,funcion,usuarios, usuarioAE,estado})  { 

    const [nombre, setNombre] = useState(usuarioAE.nombre);
    const [apellidoPaterno, setApellidoPaterno] = useState(usuarioAE.apellidoPaterno);
    const [apellidoMaterno, setApellidoMaterno] = useState(usuarioAE.apellidoMaterno);
    const [correo, setCorreo] = useState(usuarioAE.correo);
    const [contrasena, setContrasena] = useState(usuarioAE.contrasena);

    const handleNombre = (event) => {
        setNombre(event.target.value);
    } 
    
    const handleApellidoPaterno = (event) => {
        setApellidoPaterno(event.target.value);
    }

    const handleApellidoMaterno = (event) => {
        setApellidoMaterno(event.target.value);
    }

    const handleCorreo = (event) => {
        setCorreo(event.target.value);
    }

    const handleContrasena = (event) => {
        setContrasena(event.target.value);
    }


    function actualizarLista( ) {
        const idN = parseInt(id);
        const usuarioNuevo = {id: idN, nombre : nombre, apellidoPaterno : apellidoPaterno, apellidoMaterno : apellidoMaterno, correo : correo, contrasena : contrasena};

        const nuevaLista = usuarios.map((usr) => {
            if (usr.id === idN){
                return usuarioNuevo;
            }
            return usr;
        });
        funcion(nuevaLista);
        estado(false)

    }

    return (
        <div>
            <h3>Solo modifique los campos que desee editar, evite de tocar todos aquellos que esten correctos.</h3>
             <Container>
        <Row >
            <Col>
                <label>Nombre:</label>
            </Col>
            <Col>
                <input type="text" required onChange={handleNombre} defaultValue={usuarioAE.nombre}/>
            </Col>
            <Col>
                <label>Apellido Paterno:</label>
            </Col>
            <Col>
                <input type="text" required onChange={handleApellidoPaterno} defaultValue={usuarioAE.apellidoPaterno}/>
            </Col>
            <Col>
                <label>Apellido Materno:</label>
            </Col>
            <Col>
                <input type="text" required onChange={handleApellidoMaterno} defaultValue={usuarioAE.apellidoMaterno}/>
            </Col>
        </Row> 
        <Row>
            <Col>Contraseña: <input type="password" required onChange={handleContrasena} defaultValue={usuarioAE.contrasena}></input></Col>
            <Col></Col>
            <Col>Correo: <input type="email" onChange={handleCorreo} defaultValue={usuarioAE.correo}></input></Col>
        </Row>
            <Button variant="outline-light" type="submit" onClick={actualizarLista}>Guardar</Button>
        </Container>

            
       
    </div>
    )
}

