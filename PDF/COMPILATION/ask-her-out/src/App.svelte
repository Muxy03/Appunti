<script>
  import { onMount } from 'svelte';
  
  let showContent = false;
  let yesHovered = false;
  let noPosition = { x: 50, y: 50 };
  let answered = false;
  let hearts = [];
  
  onMount(() => {
    setTimeout(() => showContent = true, 300);
  });
  
  function handleYes() {
    answered = true;
    createHeartExplosion();
  }
  
  function handleNoHover() {
    // Il pulsante "No" si sposta in una posizione casuale
    noPosition = {
      x: Math.random() * 70 + 10,
      y: Math.random() * 60 + 10
    };
  }
  
  function createHeartExplosion() {
    for (let i = 0; i < 30; i++) {
      setTimeout(() => {
        hearts = [...hearts, {
          id: Date.now() + i,
          x: Math.random() * 100,
          y: Math.random() * 100,
          delay: Math.random() * 0.5,
          duration: 2 + Math.random() * 2
        }];
      }, i * 50);
    }
  }
</script>

<main class:show={showContent}>
  <div class="background">
    <div class="rose-petals">
      {#each Array(20) as _, i}
        <div class="petal" style="--delay: {i * 0.3}s; --x: {Math.random() * 100}%;"></div>
      {/each}
    </div>
  </div>
  
  {#if !answered}
    <div class="content">
      <div class="ornament top"></div>
      
      <h1 class="title">
        <span class="line">Ci sono momenti</span>
        <span class="line">in cui le parole</span>
        <span class="line">non bastano...</span>
      </h1>
      
      <div class="question-box">
        <p class="question">
          Ma questa è semplice:
        </p>
        <h2 class="big-question">
          Vorresti uscire con me?
        </h2>
      </div>
      
      <div class="buttons">
        <button 
          class="btn btn-yes" 
          class:hovered={yesHovered}
          on:mouseenter={() => yesHovered = true}
          on:mouseleave={() => yesHovered = false}
          on:click={handleYes}
        >
          <span class="btn-text">Sì! ✨</span>
        </button>
        
        <button 
          class="btn btn-no"
          on:mouseenter={handleNoHover}
          style="left: {noPosition.x}%; top: {noPosition.y}%;"
        >
          <span class="btn-text">No</span>
        </button>
      </div>
      
      <div class="ornament bottom"></div>
    </div>
  {:else}
    <div class="celebration">
      <h1 class="celebration-title">
        Non vedo l'ora! 🌹
      </h1>
      <p class="celebration-text">
        Preparati per qualcosa di speciale...
      </p>
      
      {#each hearts as heart (heart.id)}
        <div 
          class="floating-heart"
          style="left: {heart.x}%; top: {heart.y}%; animation-delay: {heart.delay}s; animation-duration: {heart.duration}s;"
        >
          ❤️
        </div>
      {/each}
    </div>
  {/if}
</main>

<style>
  main {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    opacity: 0;
    transform: scale(0.95);
    transition: all 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  
  main.show {
    opacity: 1;
    transform: scale(1);
  }
  
  .background {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: 
      radial-gradient(circle at 20% 30%, rgba(255, 182, 193, 0.3) 0%, transparent 50%),
      radial-gradient(circle at 80% 70%, rgba(255, 107, 157, 0.2) 0%, transparent 50%),
      linear-gradient(135deg, #fff8f0 0%, #ffe5ec 100%);
  }
  
  .rose-petals {
    position: absolute;
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  
  .petal {
    position: absolute;
    top: -10%;
    width: 20px;
    height: 20px;
    background: radial-gradient(ellipse at center, var(--color-rose), var(--color-blush));
    border-radius: 50% 0 50% 0;
    opacity: 0.4;
    animation: fall 15s linear infinite;
    animation-delay: var(--delay);
    left: var(--x);
  }
  
  @keyframes fall {
    to {
      top: 110%;
      transform: rotate(360deg) translateX(50px);
    }
  }
  
  .content {
    max-width: 700px;
    padding: 3rem 2rem;
    text-align: center;
    position: relative;
  }
  
  .ornament {
    width: 100px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--color-gold), transparent);
    margin: 0 auto;
    position: relative;
  }
  
  .ornament::before,
  .ornament::after {
    content: '❦';
    position: absolute;
    color: var(--color-gold);
    font-size: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
  }
  
  .ornament::before {
    left: -40px;
  }
  
  .ornament::after {
    right: -40px;
  }
  
  .ornament.top {
    margin-bottom: 3rem;
  }
  
  .ornament.bottom {
    margin-top: 3rem;
  }
  
  .title {
    font-family: var(--font-display);
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 400;
    color: var(--color-deep-rose);
    line-height: 1.3;
    margin-bottom: 3rem;
  }
  
  .title .line {
    display: block;
    opacity: 0;
    animation: fadeInUp 0.8s ease-out forwards;
  }
  
  .title .line:nth-child(1) {
    animation-delay: 0.3s;
  }
  
  .title .line:nth-child(2) {
    animation-delay: 0.6s;
  }
  
  .title .line:nth-child(3) {
    animation-delay: 0.9s;
    font-style: italic;
  }
  
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .question-box {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border: 2px solid var(--color-blush);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    margin: 2rem 0;
    box-shadow: 0 10px 40px rgba(255, 107, 157, 0.2);
    animation: fadeIn 1s ease-out 1.2s both;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  
  .question {
    font-size: 1.3rem;
    color: var(--color-midnight);
    margin-bottom: 1rem;
    font-weight: 600;
  }
  
  .big-question {
    font-family: var(--font-display);
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    color: var(--color-deep-rose);
    font-weight: 900;
    letter-spacing: -0.5px;
  }
  
  .buttons {
    position: relative;
    height: 200px;
    margin-top: 2rem;
    animation: fadeIn 1s ease-out 1.5s both;
  }
  
  .btn {
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 700;
    padding: 1.2rem 3rem;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    position: relative;
    overflow: hidden;
  }
  
  .btn-text {
    position: relative;
    z-index: 2;
  }
  
  .btn-yes {
    background: linear-gradient(135deg, var(--color-rose), var(--color-deep-rose));
    color: white;
    box-shadow: 0 10px 30px rgba(201, 24, 74, 0.3);
    position: relative;
  }
  
  .btn-yes::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, var(--color-deep-rose), #ff1744);
    opacity: 0;
    transition: opacity 0.4s;
  }
  
  .btn-yes:hover::before,
  .btn-yes.hovered::before {
    opacity: 1;
  }
  
  .btn-yes:hover,
  .btn-yes.hovered {
    transform: scale(1.15) rotate(-2deg);
    box-shadow: 0 15px 50px rgba(201, 24, 74, 0.5);
  }
  
  .btn-no {
    position: absolute;
    background: rgba(200, 200, 200, 0.3);
    color: #666;
    border: 2px solid #ccc;
    transition: all 0.3s ease;
    font-size: 1rem;
    padding: 0.8rem 2rem;
  }
  
  .btn-no:hover {
    background: rgba(200, 200, 200, 0.5);
  }
  
  .celebration {
    text-align: center;
    animation: scaleIn 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  }
  
  @keyframes scaleIn {
    from {
      opacity: 0;
      transform: scale(0.3) rotate(-10deg);
    }
    to {
      opacity: 1;
      transform: scale(1) rotate(0deg);
    }
  }
  
  .celebration-title {
    font-family: var(--font-display);
    font-size: clamp(3rem, 8vw, 6rem);
    color: var(--color-deep-rose);
    font-weight: 900;
    margin-bottom: 1.5rem;
    text-shadow: 3px 3px 0 rgba(255, 107, 157, 0.2);
  }
  
  .celebration-text {
    font-size: 2rem;
    color: var(--color-midnight);
    font-style: italic;
    font-weight: 600;
  }
  
  .floating-heart {
    position: fixed;
    font-size: 2rem;
    pointer-events: none;
    animation: floatUp 3s ease-out forwards;
    z-index: 1000;
  }
  
  @keyframes floatUp {
    0% {
      opacity: 0;
      transform: translateY(0) scale(0);
    }
    50% {
      opacity: 1;
      transform: translateY(-100px) scale(1.5) rotate(180deg);
    }
    100% {
      opacity: 0;
      transform: translateY(-300px) scale(0.5) rotate(360deg);
    }
  }
  
  @media (max-width: 768px) {
    .content {
      padding: 2rem 1.5rem;
    }
    
    .btn {
      font-size: 1.2rem;
      padding: 1rem 2rem;
    }
  }
</style>
