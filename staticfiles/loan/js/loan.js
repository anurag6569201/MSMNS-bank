// emi tool js
function calculateEMI() {
    const principal = document.getElementById('principal').value;
    const annualRate = document.getElementById('annualRate').value;
    const tenure = document.getElementById('tenure').value;

    if (principal && annualRate && tenure) {
        const monthlyRate = (annualRate / 12) / 100;
        const months = tenure * 12;

        const emi = (principal * monthlyRate * Math.pow(1 + monthlyRate, months)) / (Math.pow(1 + monthlyRate, months) - 1);

        document.getElementById('result').innerHTML = `<h4>Monthly EMI: ₹${emi.toFixed(2)}</h4>`;
    } else {
        document.getElementById('result').innerHTML = `<h4>Please fill in all fields</h4>`;
    }
}

// fd calculator tool
function calculateFDMaturity() {
    const principal = parseFloat(document.getElementById('principal').value);
    const annualRate = parseFloat(document.getElementById('annualRate').value) / 100;
    const tenure = parseFloat(document.getElementById('tenure').value);
    const n = 4;  // Quarterly compounding

    if (principal && annualRate && tenure) {
        const maturityAmount = principal * Math.pow((1 + annualRate / n), n * tenure);
        document.getElementById('result').innerHTML = `<h4>Maturity Amount: ₹${maturityAmount.toFixed(2)}</h4>`;
    } else {
        document.getElementById('result').innerHTML = `<h4>Please fill in all fields</h4>`;
    }
}