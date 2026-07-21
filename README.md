# BOTConfessions

Anonymous on-chain confession board for BOTChain. Built for **GMT Build Week Hackathon**.

## DApp Overview

- **Post** a confession — 0.001 tBOT
- **Heart** a confession — 0.001 tBOT
- All data on-chain, immutable
- Connect MetaMask, no backend needed

## Step-by-Step Deployment

### 1. MetaMask Setup
- Add network: **BOT Chain Testnet**
  - Name: `BOT Chain Testnet`
  - RPC: `https://rpc.bohr.life`
  - Chain ID: `968`
  - Symbol: `tBOT`

### 2. Get Test Tokens
- Ask organizer or BOT Chain Discord faucet for free tBOT (testnet, no real value)

### 3. Deploy Contract
- Go to [remix.ethereum.org](https://remix.ethereum.org)
- Open `BOTConfessions.sol` (or paste it new)
- Compiler → v0.8.20 → Compile
- Deploy → Environment: `Injected Provider - MetaMask` → Deploy
- Copy deployed contract address

### 4. Update Frontend
- Open `index.html`
- Replace `0x0000...0` with your deployed contract address
- Save

### 5. Deploy to Web
- Push to GitHub (done: `github.com/AtharFazli/BOTConfessions`)
- GitHub → Settings → Pages → main branch → live in 1 min
- **Buy custom domain** ($1-1.50, any extension) → GitHub Pages → Custom domain
  - Save receipt — **organizer reimburses after submission**

### 6. Submission (due Aug 4, 11:59 PM)
Submit all 4:
  1. Deployed contract address (BOT Chain)
  2. Live website URL (GitHub Pages / custom domain)
  3. GitHub repo link
  4. Demo video (2-3 min, show connect wallet → post → heart)

## Judging Criteria
| Item | Points |
|------|--------|
| Contract deployed & working | 30 |
| Anyone can connect & use | 25 |
| Unique wallets interacted | 20 |
| Use case originality | 15 |
| Demo video quality | 10 |
| **Total** | **100** |

## Files
- `BOTConfessions.sol` — Solidity contract (v0.8.20)
- `index.html` — Web3 frontend (dark theme)
