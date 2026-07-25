# BOTConfessions

Anonymous on-chain confession board for BOTChain. Built for **GMT Build Week Hackathon**.

## DApp Overview

- **Post** a confession — 0.001 tBOT
- **Heart** a confession — 0.001 tBOT
- All data on-chain, immutable
- Connect MetaMask, no backend needed

|## Step-by-Step Deployment

### 1. MetaMask Setup
- Add network: **BOT Chain Testnet**
  - Name: `BOT Chain Testnet`
  - RPC: `https://rpc.bohr.life`
  - Chain ID: `968`
  - Symbol: `tBOT`

### 2. Get Test Tokens
- Ask organizer or BOT Chain Discord faucet for free tBOT (testnet, no real value)

### 3. Deploy Contract (only if redeploying)
- Already deployed at **`0x2983b7A9BE9EACE315a0cf6A368FA3D8DDb787F3`** on BOT Chain (chain ID 968)
- To redeploy: [remix.ethereum.org](https://remix.ethereum.org) → compiler v0.8.20 → Injected Provider - MetaMask → Deploy
- Then update address in `index.html`

### 4. Deploy to Web
- Push to GitHub (done: `github.com/AtharFazli/BOTConfessions`) — auto-deploys to GitHub Pages
- Custom domain: `fazly.web.id` (buy ~$1-1.50, organizer reimburses)

### 5. Submission (due Aug 4, 11:59 PM)
Submit all 4:
  1. Deployed contract address: `0x2983b7A9BE9EACE315a0cf6A368FA3D8DDb787F3`
  2. Live website URL: `https://fazly.web.id`
  3. GitHub repo: `https://github.com/AtharFazli/BOTConfessions`
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
