<template>
  <div class="min-h-screen bg-[#FAF7F2] text-[#4B2E2B]">
    <Navbar />

    <!-- Hero Section -->
    <section class="px-16 py-20 grid md:grid-cols-2 gap-16 items-center">
      <div>
        <h1 class="text-5xl font-bold leading-tight">
          Campus Placement <br />
          <span class="text-[#8B6F5A]">Made Easy</span>
        </h1>

        <p class="mt-6 text-lg text-[#6B4F4B]">
          Connect students, companies and admin in one platform.
          Manage drives, applications and hiring seamlessly.
        </p>

        <button
          class="mt-8 bg-[#4B2E2B] text-white px-6 py-3 rounded-lg shadow hover:bg-[#6B4F4B]"
        >
          Get Started
        </button>
      </div>

      <div class="flex justify-center">
        <img
          src="https://images.unsplash.com/photo-1556761175-4b46a572b786"
          class="rounded-xl shadow-lg w-[500px]"
        />
      </div>
    </section>

    <!-- Stats Section -->
    <section class="bg-[#F3EDE4] py-14">
      <div class="grid md:grid-cols-4 text-center px-16 gap-8">
        <div>
          <h2 class="text-4xl font-bold">500+</h2>
          <p class="text-[#6B4F4B]">Students Placed</p>
        </div>
        <div>
          <h2 class="text-4xl font-bold">120+</h2>
          <p class="text-[#6B4F4B]">Companies</p>
        </div>
        <div>
          <h2 class="text-4xl font-bold">300+</h2>
          <p class="text-[#6B4F4B]">Drives Conducted</p>
        </div>
        <div>
          <h2 class="text-4xl font-bold">95%</h2>
          <p class="text-[#6B4F4B]">Success Rate</p>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="px-16 py-20">
      <h2 class="text-3xl font-bold text-center mb-12">
        Platform Features
      </h2>

      <div class="grid md:grid-cols-3 gap-10">
        <div class="bg-white p-6 rounded-xl shadow">
          <h3 class="text-xl font-semibold mb-2">For Students</h3>
          <p class="text-[#6B4F4B]">
            Apply to drives, track status, upload resumes and view placement history.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow">
          <h3 class="text-xl font-semibold mb-2">For Companies</h3>
          <p class="text-[#6B4F4B]">
            Create placement drives, shortlist candidates and manage hiring easily.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow">
          <h3 class="text-xl font-semibold mb-2">Admin Control</h3>
          <p class="text-[#6B4F4B]">
            Approve companies, monitor drives and manage complete placement data.
          </p>
        </div>
      </div>
    </section>

    <!-- Companies Section -->
    <section class="bg-[#F3EDE4] py-16 px-16">
      <h2 class="text-3xl font-bold text-center mb-10">
        Our Recruiters
      </h2>

      <div class="flex flex-wrap justify-center gap-10 opacity-80">
        <img src="https://logo.clearbit.com/google.com" class="h-10" />
        <img src="https://logo.clearbit.com/amazon.com" class="h-10" />
        <img src="https://logo.clearbit.com/microsoft.com" class="h-10" />
        <img src="https://logo.clearbit.com/tcs.com" class="h-10" />
        <img src="https://logo.clearbit.com/infosys.com" class="h-10" />
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-[#4B2E2B] text-[#EADBC8] text-center py-6">
      <p>© 2026 Placement Portal | IITM Project</p>
    </footer>
  </div>
</template>

<script setup>
import Navbar from "../components/Navbar.vue";
</script>
