import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react'
function App() {
  const initialValues = {
    data1: "",
    data2: "",
    data3: "",
    data4: "",
    data5: ""
  };
  
  //answer and print used for displaying set of answers
  const [answer, setAnswer] = useState(null)
  const [print,setPrint] = useState(false)
  //code taken from https://dev.to/deboragaleano/how-to-handle-multiple-inputs-in-react-55el
  //updates values on every change in input fields
  export default function Form() {
    const [values, setValues] = useState(initialValues);
    const handleInputChange = (e) => {
      const { name, value } = e.target;
      setValues({
        ...values,
        [name]: value,
      });
    };
    setPrint(false);
  }
  
  //function used for accessing finder program and getting an output
  function run_answer() {
    window.fetch('http://localhost:8000/get-answers?types=programming%20language&answers=python&answers=apple').then(answer => {setAnswer(answer);});
    setPrint(true);
  }
  return (
    <div className="App">

      <form>
        <input type="text" name = "data1" value = {values.data1} onChange={handleInputChange}/>
        <input type="text" name = "data2" value = {values.data2} onChange={handleInputChange}/>
        <input type="text" name = "data3" value = {values.data3} onChange={handleInputChange}/>
        <input type="text" name = "data4" value = {values.data4} onChange={handleInputChange}/>
        <input type="text" name = "data5" value = {values.data4} onChange={handleInputChange}/>

      </form>
      <button onClick={()=>run_answer()} >Submit</button>
      {
        print?
        <h1>{answer}</h1>
        :null
      }

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
