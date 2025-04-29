import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [rules, setRules] = useState([]);
  
  useEffect(() => {
    fetch('https://tmqcqm7lha.execute-api.ap-northeast-1.amazonaws.com/prod/naming',{
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        // 他にも必要なヘッダーがあれば追加
      },
    })
      .then(response => response.json())
      .then(data => setRules(data.rules))
      .catch(error => console.error('Error fetching rules:', error));
  }, []);

  return (
    <div className="App">
      <h1>Naming Generator</h1>
      <ul>
        {rules.map((rule, index) => (
          <li key={index}>{rule}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
