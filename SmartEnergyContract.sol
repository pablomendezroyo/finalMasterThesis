pragma solidity ^0.6.4;

contract EnergySmartContract {
    
    struct OfferSeller{
        address addressSeller;
        uint amount_min_kw;
        uint amount_max_kw;
        uint price_min_kwh;
    }
    
    struct OfferBuyer{
        address addressBuyer;
        uint amount_kw;
        uint price_max_kwh;
    }
    
    struct Payment{
        uint amount;
        uint timestamps;
    }
    struct Balance{
        uint totalBalance;
        uint numPayments;
        mapping(uint => Payment) payments;
    }
    
    mapping(address => OfferSeller) public seller;
    mapping(address => OfferBuyer) public buyer;
    mapping(address => Balance) public balanceReceived;
    
    OfferSeller[] public Offers_Seller_Array;
    
    function getBalance() public view returns(uint){
        return address(this).balance;
    }
    
    function sendMoney() public payable{
        balanceReceived[msg.sender].totalBalance += msg.value; 
        Payment memory payment = Payment(msg.value, now);
        balanceReceived[msg.sender].payments[balanceReceived[msg.sender].numPayments] = payment;
        
        balanceReceived[msg.sender].numPayments ++;
    }
    
    function setSeller(address _addressSeller, uint _amount_min_kw, uint _amount_max_kw, uint _price_min_kwh) public {
        seller[msg.sender].addressSeller = _addressSeller;
        seller[msg.sender].amount_min_kw = _amount_min_kw;
        seller[msg.sender].amount_max_kw = _amount_max_kw;
        seller[msg.sender].price_min_kwh = _price_min_kwh;
        //Offers_Seller_Array.push(_addressSeller, _amount_min_kw, _amount_max_kw, _price_min_kwh);
        Offers_Seller_Array.push(OfferSeller({addressSeller: _addressSeller, amount_min_kw: _amount_min_kw, amount_max_kw: _amount_max_kw, price_min_kwh: 100}));
    }
    
    function setBuyer(address _addressBuyer, uint _amount_kw, uint _price_max_kwh) public {
        require(balanceReceived[msg.sender].totalBalance > 0);
        require(balanceReceived[msg.sender].totalBalance >= _amount_kw * _price_max_kwh);
        buyer[msg.sender].addressBuyer = _addressBuyer;
        buyer[msg.sender].amount_kw = _amount_kw;
        buyer[msg.sender].price_max_kwh = _price_max_kwh;
    }
    
    
}