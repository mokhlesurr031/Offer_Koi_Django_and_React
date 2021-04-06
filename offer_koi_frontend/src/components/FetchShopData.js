import React from "react";

class FetchShopData extends React.Component {
  state = {
    loading: true,
    shop_name: null,
  };
  async componentDidMount() {
    const url = "http://127.0.0.1:8000/shops/api_data/";
    const response = await fetch(url);
    const data = await response.json();
    this.setState({ shop_name: data[0].name });
    // console.log(data[0].name);
  }

  render() {
    return (
      <div>
        {/* {this.state.loading ? <div>Loading...</div> :  */}
        <div> {this.state.shop_name} </div>
      </div>
    );
  }
}

export default FetchShopData;
