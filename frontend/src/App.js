
import { useState } from 'react';
import "./index.css";
import Title from './Title';
import Autocomplete from './Autocomplete';


function App() {

  const [typeList, setTypeList] = useState(['']);
  const [answerList, setAnswerList] = useState(['']);
  const [scoresList, setscoresList] = useState([]);
  
  async function getScores() {
    const apiUrl = 'http://localhost:8000/get-sparql?';
    let searchParams = new URLSearchParams();
    console.log("entered getScores");

    typeList.forEach(type => {
      searchParams.append('types', type);
    });

    answerList.forEach(answer => {
      searchParams.append('answers', answer);
    });


    fetch(apiUrl + searchParams.toString())
			.then((response) => response.json())
			.then((data) => {
        console.log("setting data");
				setscoresList(data) // new
		});

    console.log("done fetching");
    console.log("scores"+ scoresList);

    // const response = await fetch(apiUrl + searchParams.toString());
    
    // response.json().then(
    //   (result) => { 
    //     setscoresList(result);
    //     console.log("result:"+feresult);
    //   },
    //   (error) => { 
    //      console.log("Promise error:"+error);
    //   },
    // );
    // console.log("scoresList: "+ scoresList);
  };

  // handle input change
  const handleInputChange = (newValue, index, currList, setFunction) => {
    // const { name, value } = e.target;
    let list = [...currList];
    list[index] = newValue;
    setFunction(list);
  };

  // handle click event of the Remove button
  const handleRemoveClick = (index, currList, setFunction) => {
    let list = [...currList];
    list.splice(index, 1);
    setFunction(list);
  };

  // handle click event of the Add button
  const handleAddClick = (currList, setFunction) => {
    setFunction([...currList, '']);
  };


  return (
    <div className="form-container">
      <link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Lora&display=swap" rel="stylesheet"/>
      <Title />

      <h2>Answer Type</h2>
      {typeList.map((x, i) => (
        <div className="form-field">
          <Autocomplete
            input={x}
            setInput={val => handleInputChange(val, i, typeList, setTypeList)}
          />

          {typeList.length !== 1 && <button
          className="button submit"
          onClick={() => handleRemoveClick(i, typeList, setTypeList)}>Remove</button>}
          {typeList.length - 1 === i && <button onClick={() => handleAddClick(typeList, setTypeList)}>Add</button>}
            

        </div>
      ))}

      <h2>Options</h2>
      {answerList.map((x, i) => (
        <div className="form-field">
          <Autocomplete
            input={x}
            setInput={val => handleInputChange(val, i, answerList, setAnswerList)}
          />

          {answerList.length !== 1 && <button
          className="button submit"
          onClick={() => handleRemoveClick(i, answerList, setAnswerList)}>Remove</button>}
          {answerList.length - 1 === i && <button onClick={() => handleAddClick(answerList, setAnswerList)}>Add</button>}
            


        </div>
      ))}
      <button className="button submit" type="submit" onClick={() => getScores()}>Submit</button>
     
     { scoresList.length > 0 ? <div>
        <h2>Accuracy Scores</h2>
            {console.log(scoresList.length)}
            <ul>
              {scoresList.map((s, i) => <li key={i} >{answerList[i]}: {s}</li>)}
            </ul>
      </div> : null}
      
      
    </div>
  );
}

export default App;
