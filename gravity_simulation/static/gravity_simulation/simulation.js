const c = document.getElementById('c');
const ctx = c.getContext('2d');
const particles = [];
const gravityPoints = [];

c.width = window.innerWidth;
c.height = window.innerHeight;

window.addEventListener('resize', () => {
    c.width = window.innerWidth;
    c.height = window.innerHeight;
});

class Particle {
    constructor(x, y, vx, vy, mass, color) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
        this.mass = mass;
        this.radius = Math.sqrt(mass) * 2;
        this.color = color;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
    }
}

class GravityPoint {
    constructor(x, y, mass, color) {
        this.x = x;
        this.y = y;
        this.mass = mass;
        this.radius = Math.sqrt(mass) * 5;
        this.color = color;
    }

    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.strokeStyle = 'rgba(255,255,255,0.3)';
        ctx.stroke();
    }
}

function createParticles(count) {
    for (let i = 0; i < count; i++) {
        const x = Math.random() * c.width;
        const y = Math.random() * c.height;
        const vx = (Math.random() - 0.5) * 2;
        const vy = (Math.random() - 0.5) * 2;
        const mass = Math.random() * 5 + 1;
        const color = `hsl(${Math.random() * 360}, 100%, 70%)`;
        particles.push(new Particle(x, y, vx, vy, mass, color));
    }
}

function calculateGravity() {
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        let fx = 0;
        let fy = 0;

        for (let j = 0; j < gravityPoints.length; j++) {
            const gp = gravityPoints[j];

            const dx = gp.x - p.x;
            const dy = gp.y - p.y;
            const distanceSq = dx * dx + dy * dy;
            const distance = Math.sqrt(distanceSq);

            if (distance < p.radius + gp.radius) { // Collision detection
                // Simple collision: remove particle
                particles.splice(i, 1);
                i--;
                continue;
            }

            const G = 0.5; // Gravitational constant
            const force = G * ((p.mass * gp.mass) / distanceSq);

            fx += force * (dx / distance);
            fy += force * (dy / distance);
        }

        p.vx += fx / p.mass;
        p.vy += fy / p.mass;
    }
}

c.addEventListener('click', (e) => {
    const mass = Math.random() * 500 + 100; // Larger mass for gravity points
    const color = `rgba(255, 255, 255, 0.8)`;
    gravityPoints.push(new GravityPoint(e.clientX, e.clientY, mass, color));
});

createParticles(100); // Initial particles

function animate() {
    ctx.clearRect(0, 0, c.width, c.height);
    // ctx.fillStyle = 'rgba(0, 0, 0, 0.1)'; // Fading trail effect
    // ctx.fillRect(0, 0, c.width, c.height);

    calculateGravity();

    for (const p of particles) {
        p.update();
        p.draw();
    }

    for (const gp of gravityPoints) {
        gp.draw();
    }

    requestAnimationFrame(animate);
}

animate();