import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/auth'
import Main from './components/mainLayout';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Profile from './components/profile';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Login/>}/>
          <Route path='/main' element={<Main/>}>
             <Route path="profile" element={<Profile />} />
          </Route>
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;
