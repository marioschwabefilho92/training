import React from 'react'
import './register.css'
var bcrypt = require('bcryptjs');
var salt = bcrypt.genSaltSync(10);


export default class Register extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            password: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value });
    }

    handleSubmit(event) {
        event.preventDefault();
        bcrypt.hash(this.state.password, salt).then((result) => {
            //pass result to db
            console.log(result)
            // bcrypt.compare("teste", result).then((res)=>{
            //     console.log(res)
            // })
        });
    }

    render() {
        return (
            <div className="login-container">
                <form className="form-container" onSubmit={this.handleSubmit}>
                    <label>
                        Username:
                        <input 
                            type="text" 
                            name="username"
                            value={this.state.username} 
                            onChange={this.handleChange} 
                        />
                    </label>
                    <label>
                        Password:
                        <input 
                            type="text" 
                            name="password"
                            value={this.state.password} 
                            onChange={this.handleChange} 
                        />
                    </label>
                    <input type="submit" value="Register" />
                </form>
            </div>
        );
    }
}