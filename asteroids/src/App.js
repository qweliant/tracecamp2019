import React from 'react';
import './App.css';
import { getAsteroids } from './nasaWorker';

function App() {

  console.log(getAsteroids("2018-06-13", "2019-01-01"))
  return (
    <div className="App">
      Test
    </div>
  );
}

export default App;