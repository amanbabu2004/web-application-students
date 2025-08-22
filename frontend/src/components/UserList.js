import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { userService } from '../services/api';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [message, setMessage] = useState('');
  const [messageType, setMessageType] = useState('');

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      const data = await userService.getAllUsers();
      setUsers(data);
      setMessage('');
    } catch (error) {
      setMessage('Failed to fetch users');
      setMessageType('error');
      console.error('Error fetching users:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id, name) => {
    if (window.confirm(`Are you sure you want to delete ${name}?`)) {
      try {
        await userService.deleteUser(id);
        setMessage(`User ${name} deleted successfully`);
        setMessageType('success');
        fetchUsers(); // Refresh the list
      } catch (error) {
        setMessage('Failed to delete user');
        setMessageType('error');
        console.error('Error deleting user:', error);
      }
    }
  };

  if (loading) {
    return (
      <div className="container">
        <div className="loading">Loading users...</div>
      </div>
    );
  }

  return (
    <div className="container">
      <h2>All Users</h2>
      
      {message && (
        <div className={`message ${messageType}`}>
          {message}
        </div>
      )}

      {users.length === 0 ? (
        <p>No users found. <Link to="/add">Add the first user</Link></p>
      ) : (
        <table className="user-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Email</th>
              <th>Age</th>
              <th>Occupation</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>{user.age}</td>
                <td>{user.occupation}</td>
                <td>
                  <div className="actions">
                    <Link to={`/edit/${user.id}`} className="btn btn-primary">
                      Edit
                    </Link>
                    <button
                      onClick={() => handleDelete(user.id, user.name)}
                      className="btn btn-danger"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default UserList;
