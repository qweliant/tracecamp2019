import React, {useState} from 'react';
import './App.css';
import getCurrency from './coinbaseAPI'


function App() {
  const [value, setValue] = useState([])
  const [rates, setRates] = useState([])
  const [currency, setCurrency] = useState("USD")

  React.useEffect(() => { 
    getCurrency(currency)
    .then(res => {
      setRates(res.data.data.rates)
      
      //data = res.data.Object.toString
      //console.log(data)
      //setValue(JSON.stringify(data))
    })
    .catch(err => {
      console.log(err)
    })
   }, [currency])
  
   console.log(rates)

  return (
    <div className="App">
      <div>
        
      </div>
    </div>
  );
}

export default App;
