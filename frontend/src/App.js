import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react'
import get_answer from 'finder'
function App() {
  const initialValues = {
    data1: "",
    data2: "",
    data3: "",
    data4: "",
  };

  const [print,setPrint] = useState(false)
  //code taken from https://dev.to/deboragaleano/how-to-handle-multiple-inputs-in-react-55el
  export default function Form() {
    const [values, setValues] = useState(initialValues);
    const [print, setPrint] = useState(false);
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setValues({
        ...values,
        [name]: value,
      });
    };
  }
  
  function run_answer() {
    get_answer(initialValues)
  }
  return (
    <div className="App">
      {
        print?
        <h1>Get Input box value !</h1>
        :null
      }
      <form>
        <input type="text" name = "data1" value = {values.data1} onChange={handleInputChange}/>
        <input type="text" name = "data2" value = {values.data2} onChange={handleInputChange}/>
        <input type="text" name = "data3" value = {values.data3} onChange={handleInputChange}/>
        <input type="text" name = "data4" value = {values.data4} onChange={handleInputChange}/>

      </form>


      <button onClick={()=>run_answer()} >Submit</button>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
