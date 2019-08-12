import React from "react";
import Landing from './Landing';
import {MDBContainer, MDBRow, MDBCard, MDBCardTitle, MDBBtn, MDBCardGroup, MDBCardImage, MDBCardText, MDBCardBody } from "mdbreact";
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import index from '../images/index.png';
import logo3 from '../images/logo3.jpg';
import bloom2 from '../images/bloom2.jpg';
import bloom from '../images/bloom.jpg';
import tmdb from '../images/tmdb.png';
import yang from '../images/yang.png';

import { CardColumns, Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

console.log(index);
const cards=[
  {
    title: "lmbk",
    short: "Gathering garmin user stress data and presenting levels to confront stress in team environments, and provide workable solutions",
    path: "",
    to:"",
    image: index,
  }, 

  {
    title: "metavisuo",
    short: "One stop for csv backend model creation, training, and visualization",
    path: "",
    to:"",
    image: bloom,

  },

  {
    title: "tmdb data visuaalization",
    short: "Proof of metavisuo, creating prdictive models from kaggle csv set of movies",
    path: "",
    to:"",
    image: bloom2,
  }, 

  {
    title: "Georgetown Neurology Handbook",
    short: "Transferring text handbooks to web/phone apps for GNH, DC",
    path: "",
    to:"",
    image: logo3,
  }, 
  
  {
    title: "YangGang SC Map",
    short: "Create map for Yang supporters in SC to view and support each other",
    path: "",
    to:"",
    image: yang,
  },
  
  {
    title: "random-tmdb-movie-api",
    short: "Hello moto",
    path: "",
    to:"Home",
    image: tmdb,
  }, 
]

const tools=[

  {
    title: "react",

  },

  {
    title: "django",

  }, 

  {
    title: "heroku",

  }, 

  {
    title: "postgres",

  },

  {
    title: "github",

  },

  {
    title: "Surge",

  },
  
  {
    title: "mdbootstrap, material ui, shards-react",

  },

  {
    title: "JSX, javascript, python, c++/c, html, css, JSON, ",

  },


]

const tStyle ={
  textAlign: 'center',
  fontSize: '6.5em',
  fontFamily: "Sans-serif",
  
};

const bStyle ={
  textAlign: 'center',
  fontSize: '4.5em',
  color: 'white',
  backgroundColor: 'black',

}
const HomeView = () => {
    const [spacing, setSpacing] = React.useState(2);
    
    
    
    return (
      
      <main >
      
      <Landing/>
      

      <h1 style={tStyle} >Qwelian Damarius Tanner</h1>
        <h2 style={bStyle}>
          As a software developer my goal is to provide specific solutions to 
          diverse probelms we face in the new era of understanding technology. 
          Deconstructing paradigms as a enduring student of science, social schemas, and lived experiences is my passion.  
        </h2>
                

          
      <CardColumns>
        { cards.map((card,index) => (
          <Grid key={card} item>        
            <MDBCard style={{ width: "35rem" }}>
              <MDBCardImage className="img-fluid" src={card.image } alt={card.title} waves />
                <MDBCardBody>
                  <MDBCardTitle>{card.title}</MDBCardTitle>
                    <MDBCardText>
                      {card.short}
                        </MDBCardText>
                          <MDBBtn color="red" size="md">
                            view
                          </MDBBtn>
                        </MDBCardBody>
                      </MDBCard>
                      
                      </Grid>
                )) }

      </CardColumns>
      </main>
      
      
     
    );
}

export default HomeView;