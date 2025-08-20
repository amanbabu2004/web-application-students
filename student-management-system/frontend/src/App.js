import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './Login';

function App() {
  return (
    <Router>
      <div>
        <h1>Student Management System</h1>
        <Switch>
          <Route path="/login" component={Login} />
          {/* Additional routes can be added here */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;