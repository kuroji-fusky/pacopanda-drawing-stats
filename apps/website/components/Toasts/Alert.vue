<template>
  <div class="p-4 bg-red-500 border-red-300">
    <ContentSlot :use="$slots.default" unwrap="p" />
  </div>
</template>
