<template>
  <div class="min-h-screen flex bg-gray-100">

    <!-- Sidebar -->
    <aside class="w-64 bg-blue-700 text-white flex flex-col">
      <div class="p-6 text-2xl font-bold border-b border-blue-500">
        Placement Portal
      </div>

      <nav class="flex-1 p-4 space-y-3">
        <div class="hover:bg-blue-600 p-3 rounded cursor-pointer">Dashboard</div>
        <div class="hover:bg-blue-600 p-3 rounded cursor-pointer">Students</div>
        <div class="hover:bg-blue-600 p-3 rounded cursor-pointer">Companies</div>
        <div class="hover:bg-blue-600 p-3 rounded cursor-pointer">Drives</div>
        <div class="hover:bg-blue-600 p-3 rounded cursor-pointer">Applications</div>
      </nav>

      <div class="p-4 border-t border-blue-500">
        <button
          @click="logout"
          class="w-full bg-white text-blue-700 py-2 rounded font-semibold"
        >
          Logout
        </button>
      </div>
    </aside>


    <!-- Main Content -->
    <div class="flex-1 flex flex-col">

      <!-- Top Navbar -->
      <header class="bg-white shadow px-8 py-4 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-gray-700">Admin Dashboard</h1>

        <div class="flex items-center gap-4">
          <img
            src="https://i.pravatar.cc/40"
            class="w-10 h-10 rounded-full"
          />
        </div>
      </header>


      <!-- Content -->
      <main class="p-8 flex-1 overflow-y-auto">

        <!-- Stats Cards -->
        <div class="grid grid-cols-4 gap-6 mb-10">
          <div class="bg-white p-6 rounded-lg shadow">
            <p class="text-gray-500">Students</p>
            <h2 class="text-3xl font-bold text-blue-600">
              {{ stats.total_students || 0 }}
            </h2>
          </div>

          <div class="bg-white p-6 rounded-lg shadow">
            <p class="text-gray-500">Companies</p>
            <h2 class="text-3xl font-bold text-green-600">
              {{ stats.total_companies || 0 }}
            </h2>
          </div>

          <div class="bg-white p-6 rounded-lg shadow">
            <p class="text-gray-500">Drives</p>
            <h2 class="text-3xl font-bold text-purple-600">
              {{ stats.total_drives || 0 }}
            </h2>
          </div>

          <div class="bg-white p-6 rounded-lg shadow">
            <p class="text-gray-500">Applications</p>
            <h2 class="text-3xl font-bold text-red-600">
              {{ stats.total_applications || 0 }}
            </h2>
          </div>
        </div>


        <!-- Banner Section (Internshala style) -->
        <div class="bg-blue-600 text-white rounded-lg p-8 flex justify-between items-center mb-10">
          <div>
            <h2 class="text-3xl font-bold mb-2">
              Campus Placement Made Easy
            </h2>
            <p class="text-blue-100">
              Manage drives, students, and hiring from one place.
            </p>
          </div>

          <img
            src="https://images.unsplash.com/photo-1522071820081-009f0129c71c"
            class="w-64 rounded-lg shadow"
          />
        </div>


        <!-- Recent Activity -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-bold mb-4">Recent Activity</h2>

          <table class="w-full">
            <thead class="bg-gray-100">
              <tr>
                <th class="text-left p-3">Student</th>
                <th class="text-left p-3">Drive</th>
                <th class="text-left p-3">Status</th>
              </tr>
            </thead>

            <tbody>
              <tr class="border-b">
                <td class="p-3">John Doe</td>
                <td class="p-3">Google SDE</td>
                <td class="p-3 text-green-600 font-semibold">Applied</td>
              </tr>

              <tr class="border-b">
                <td class="p-3">Priya Sharma</td>
                <td class="p-3">Amazon Analyst</td>
                <td class="p-3 text-blue-600 font-semibold">Shortlisted</td>
              </tr>
            </tbody>
          </table>
        </div>

      </main>
    </div>

  </div>
</template>


<script setup lang="ts">
import { ref, onMounted } from "vue";
import api from "../api/api";
import { useRouter } from "vue-router";

const router = useRouter();

const stats = ref<any>({});

onMounted(async () => {
  try {
    const res = await api.get("/admin/dashboard");
    stats.value = res.data;
  } catch (e) {
    console.log("Dashboard load error");
  }
});

const logout = () => {
  localStorage.removeItem("token");
  router.push("/login");
};
</script>
