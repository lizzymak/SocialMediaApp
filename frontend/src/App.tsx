import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/auth'
import Home from './components/home';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      {/* <Login></Login> */}
      <Router>
        <Routes>
          <Route path='/' element={<Login/>}/>
          <Route path='/home' element={<Home/>}/>
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;
