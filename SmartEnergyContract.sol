pragma solidity ^0.6.4;

contract EnergySmartContract {
    
    struct OfferSeller{
        address payable addressSeller;
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
    OfferBuyer[] public Offers_Buyer_Array;
    
    event matchFound(bool _status);
    
    function getBalance() public view returns(uint){
        return address(this).balance;
    }
    
    function sendMoney() public payable{
        balanceReceived[msg.sender].totalBalance += msg.value; 
        Payment memory payment = Payment(msg.value, now);
        balanceReceived[msg.sender].payments[balanceReceived[msg.sender].numPayments] = payment;
        
        balanceReceived[msg.sender].numPayments ++;
    }
    
    function setSeller(uint _amount_min_kw, uint _amount_max_kw, uint _price_min_kwh) public {
        seller[msg.sender].addressSeller = msg.sender;
        seller[msg.sender].amount_min_kw = _amount_min_kw;
        seller[msg.sender].amount_max_kw = _amount_max_kw;
        seller[msg.sender].price_min_kwh = _price_min_kwh;
       
        Offers_Seller_Array.push(OfferSeller({addressSeller: msg.sender, amount_min_kw: _amount_min_kw, amount_max_kw: _amount_max_kw, price_min_kwh: _price_min_kwh}));
        matchBuyer(msg.sender, _amount_min_kw, _amount_max_kw, _price_min_kwh);
    }
    
    function setBuyer(uint _amount_kw, uint _price_max_kwh) public {
        require(balanceReceived[msg.sender].totalBalance > 0, "The balance should be greater than 0");
        require(balanceReceived[msg.sender].totalBalance >= _amount_kw * _price_max_kwh, "The balance should be greater or equal than the offer (amount * price)");
        buyer[msg.sender].addressBuyer = msg.sender;
        buyer[msg.sender].amount_kw = _amount_kw;
        buyer[msg.sender].price_max_kwh = _price_max_kwh;
        
        Offers_Buyer_Array.push(OfferBuyer({addressBuyer: msg.sender, amount_kw: _amount_kw, price_max_kwh: _price_max_kwh}));
        matchSeller(msg.sender, _amount_kw, _price_max_kwh);
    }
    
    function matchSeller(address _buyer, uint _amount_kw, uint _price_max_kwh) internal {
        for(uint i = 0; i < Offers_Seller_Array.length; i++){
                if(_amount_kw <= Offers_Seller_Array[i].amount_max_kw 
                && _amount_kw >= Offers_Seller_Array[i].amount_min_kw 
                && _price_max_kwh >= Offers_Seller_Array[i].price_min_kwh){
                    withdrawMoney(Offers_Seller_Array[i].addressSeller, _buyer, 10**18*_amount_kw*Offers_Seller_Array[i].price_min_kwh);
                    deleteSeller(i);
                    deleteBuyer(Offers_Buyer_Array.length-1);
                }
            }
    }
    
    function matchBuyer(address payable _seller, uint _amount_min_kw, uint _amount_max_kw, uint _price_min_kwh) internal {
        for(uint i = 0; i < Offers_Buyer_Array.length; i++){
                if(_amount_min_kw <= Offers_Buyer_Array[i].amount_kw 
                && _amount_max_kw >= Offers_Buyer_Array[i].amount_kw 
                && _price_min_kwh <= Offers_Buyer_Array[i].price_max_kwh){
                    withdrawMoney(_seller, Offers_Buyer_Array[i].addressBuyer, 10**18*Offers_Buyer_Array[i].amount_kw*_price_min_kwh);
                    deleteBuyer(i);
                    deleteBuyer(Offers_Seller_Array.length-1);
                }
            }
    }
    
    function withdrawMoney(address payable _to, address _from, uint _amount) internal {
        require(_amount <= balanceReceived[_from].totalBalance, "You don´t have enough ether");
        assert(balanceReceived[_from].totalBalance >= balanceReceived[_from].totalBalance - _amount);
        balanceReceived[_from].totalBalance -= _amount;
        _to.transfer(_amount);
    }
    
    function deleteSeller(uint _index) internal{
        delete Offers_Seller_Array[_index];
    }
    
    function deleteBuyer(uint _index) internal{
        delete Offers_Buyer_Array[_index];
    }
    
    function convertWeiToEther(uint _amountInWei) public pure returns(uint){
        return _amountInWei / 1 ether;
    }
    
}