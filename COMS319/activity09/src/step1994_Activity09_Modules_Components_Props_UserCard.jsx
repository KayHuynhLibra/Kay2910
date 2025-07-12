// Author: Kim Sang Huynh
// ISU Netid: step1994@iastate.edu
// Date: March 28th, 2025

import 'bootstrap/dist/css/bootstrap.css';
import { Container, Card, Col, Button } from 'react-bootstrap';

export function UserCard(props) {
  return (
    <>
      <Container className="p-4">
        <Card style={{ width: '25rem' }}>
          <Card.Img className="card-img-top" src={props.picture} alt={props.name} />
          <Card.Body>
            <Card.Title className="card-title">{props.name}</Card.Title>
            <Card.Text className="card-text">${props.salary}</Card.Text>
            <Card.Text className="card-text">{props.status ? "Married" : "Single"}</Card.Text>
            <ul>
              <li><Card.Text className="card-text">Street: {props.address.street}</Card.Text></li>
              <li><Card.Text className="card-text">City: {props.address.city}</Card.Text></li>
              <li><Card.Text className="card-text">State: {props.address.state}</Card.Text></li>
            </ul>
          </Card.Body>
        </Card>
      </Container>
    </>
  );
}