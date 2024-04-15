import Table from 'react-bootstrap/Table';


export const VerUsuarios = ({usuarios}) => {
    return (
        <div>
        <h1>Lista de Usuarios</h1>



<Table striped bordered hover size="sm" variant="dark">
      <thead>
        <tr>
          <th>id</th>
          <th>Nombre</th>
          <th>Apellido Paterno</th>
          <th>Apellido Materno</th>
          <th>Correo</th>
        </tr>
      </thead>
      <tbody>
      {usuarios.map((usr, key)=>{
                    return(
                        <tr key={key}>
                            <td>{usr.id}</td>
                            <td>{usr.nombre}</td>
                            <td>{usr.apellidoPaterno}</td>
                            <td>{usr.apellidoMaterno}</td>
                            <td>{usr.correo}</td>
                        </tr>
                    );
                })}
      </tbody>
    </Table>


        </div>
    );
}