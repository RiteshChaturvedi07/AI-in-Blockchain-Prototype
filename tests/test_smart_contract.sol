// test_smart_contract.sol
pragma solidity ^0.8.0;

import "remix_tests.sol"; // Required for testing in Remix IDE
import "./smart_contract.sol"; // Import the actual smart contract

contract TestSmartContract {
    SimpleContract simpleContract;

    function beforeEach() public {
        simpleContract = new SimpleContract();
    }

    // Test deposit function
    function testDeposit() public {
        uint initialBalance = address(this).balance;
        simpleContract.deposit{value: 1 ether}();
        Assert.equal(simpleContract.balances(address(this)), 1 ether, "Deposit failed!");
    }

    // Test withdrawal function
    function testWithdraw() public {
        simpleContract.deposit{value: 1 ether}();
        simpleContract.withdraw(0.5 ether);
        Assert.equal(simpleContract.balances(address(this)), 0.5 ether, "Withdraw failed!");
    }

    // Test check balance
    function testCheckBalance() public {
        simpleContract.deposit{value: 1 ether}();
        Assert.equal(simpleContract.checkBalance(), 1 ether, "Balance check failed!");
    }
}
