import logo from './logo.svg';
//import './App.css';
import { useState } from 'react';
import "./index.css";
import Title from './Title';
import Autocomplete from './Autocomplete';

function App() {
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

      <Autocomplete />

      <input
          id="answertype"
          className="form-field"
          type="text"
          placeholder="Expected Answer Type"
          name="answertype"
        />

      {inputList.map((x, i) => {
        return (

          <div className="form-field">

            <input
              name="firstName"
              placeholder="Enter a option"
              value={x.firstName}
              onChange={e => handleInputChange(e, i)}
            />


              {inputList.length !== 1 && <button
                className="button submit"
                onClick={() => handleRemoveClick(i)}>Remove</button>}
              {inputList.length - 1 === i && <button onClick={handleAddClick}>Add</button>}

          </div>
        );
      })}
      <button className="button submit" type="submit">Submit</button>

    </div>
  );




}

export default App;
