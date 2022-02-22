import logo from './logo.svg';
//import './App.css';
import { useState } from 'react';
import "./index.css";
import Title from './Title';

function App() {
  async function getPossibleNodes() {
    const apiUrl = 'https://www.wikidata.org/w/api.php?';
    let params = {
      action: 'wbsearchentities',
      search: 'python',  // TODO: get from state of question type input
      language: 'en',
      format: 'json',
      origin: '*'
    };
    let searchParams = new URLSearchParams(params);

    const response = await fetch(apiUrl + searchParams.toString());
    return response.json()
  };

  async function getScores() {
    const apiUrl = 'http://localhost:8000/get-sparql?';
    let searchParams = new URLSearchParams();
    // TODO: append types and answers to searchParams
    searchParams.append('types', 'programming language');
    searchParams.append('types', 'scripting language');
    searchParams.append('answers', 'java');
    searchParams.append('answers', 'python');
    searchParams.append('answers', 'false');

    const response = await fetch(apiUrl + searchParams.toString());
    return response.json()
  };

  console.log(getPossibleNodes());
  console.log(getScores());

  /* return (

  <div className="form-container">

      <form className="register-form">

      <Title />

        <input
          id="question"
          className="form-field"
          type="text"
          placeholder="Question"
          name="question"
        />

        <button className="form-field" type="submit">
          Option - 1
        </button>

        <button className="form-field" type="submit">
          Option - 2
        </button>

        <button className="form-field" type="submit">
          Option - 3
        </button>

        <button className="form-field" type="submit">
          Option - 4
        </button>



      </form>
    </div>
  ); */

  const [inputList, setInputList] = useState([{ options: "" }]);

  // handle input change
  const handleInputChange = (e, index) => {
    const { name, value } = e.target;
    const list = [...inputList];
    list[index][name] = value;
    setInputList(list);
  };

  // handle click event of the Remove button
  const handleRemoveClick = index => {
    const list = [...inputList];
    list.splice(index, 1);
    setInputList(list);
  };

  // handle click event of the Add button
  const handleAddClick = () => {
    setInputList([...inputList, { options: "" }]);
  };

  return (
    <div className="form-container">
      <Title />
      {inputList.map((x, i) => {
        return (
          <div className="form-field">
            <input
              name="firstName"
              placeholder="Enter First Name"
              value={x.firstName}
              onChange={e => handleInputChange(e, i)}
            />
            
            <div className="form-container">
              {inputList.length !== 1 && <button
                className="form-field"
                onClick={() => handleRemoveClick(i)}>Remove</button>}
              {inputList.length - 1 === i && <button onClick={handleAddClick}>Add</button>}
            </div>
          </div>
        );
      })}
      <div style={{ marginTop: 20 }}>{JSON.stringify(inputList)}</div>
    </div>
  );




}

export default App;
