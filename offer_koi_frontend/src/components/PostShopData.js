import React, { Component } from "react";
import axios from "axios";

class PostShopData extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "",
      location: "",
      contact: "",
    };
  }

  changeHandler = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  submitHandler = (e) => {
    e.preventDefault();
    console.log(this.state);
    axios
      .post("http://127.0.0.1:8000/shops/api_data/", this.state)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  render() {
    const { name, location, contact } = this.state;
    return (
      <div>
        <form onSubmit={this.submitHandler}>
          <div>
            <input
              type="text"
              name="name"
              value={name}
              onChange={this.changeHandler}
            />
          </div>
          <div>
            <input
              type="text"
              name="location"
              value={location}
              onChange={this.changeHandler}
            />
          </div>
          <div>
            <input
              type="text"
              name="contact"
              value={contact}
              onChange={this.changeHandler}
            />
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default PostShopData;
