import React from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './components/auth'
import Main from './components/mainLayout';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Profile from './components/profile';
import Home from './components/home';
import Search from './components/searchPage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<Login/>}/>
          <Route path='/main' element={<Main/>}>
              <Route path="home" element={<Home />} />
              <Route path="profile" element={<Profile />} />
              <Route path="search" element={<Search />} />
          </Route>
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;
